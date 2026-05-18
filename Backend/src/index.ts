import express, { Request, Response } from 'express';
import cors from 'cors';
import { collections, connectToDatabase } from './services/database.service';
import Achievement from './models/achievement';
import Filter from './models/filter';
import * as dotenv from 'dotenv';
import * as nodestone from '@xivapi/nodestone';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;
const frontendURL = process.env.FRONTEND_URL || 'http://localhost:5173';

const corsOptions = {
	origin: frontendURL,
	optionsSuccessStatus: 200
};

// Middleware to parse JSON bodies
app.use(express.json());
app.use(cors(corsOptions));

app.get('/lodestone/character/:id', async (req: Request, res: Response) => {
	const characterParser = new nodestone.Character();
	try {
		const characterData = await characterParser.parse({ params: { characterId: req.params.id } } as any);
		res.status(200).json(characterData);
	} catch (error) {
		res.status(500).json({ message: 'An error occurred while fetching character data.', error: error instanceof Error ? error.message : 'Unknown error' });
	}
});

app.get('/lodestone/character_achievements/:id', async (req: Request, res: Response) => {
	const achievementParser = new nodestone.Achievements();
	try {
		const achievementData = await achievementParser.parse({ params: { characterId: req.params.id} } as any);
		res.status(200).json(achievementData);
	} catch (error) {
		res.status(500).json({ message: 'An error occurred while fetching character data.', error: error instanceof Error ? error.message : 'Unknown error' });
	}
});

app.get('/achievements', async (req: Request, res: Response) => {
	try{
		const filter = new Filter(
			req.query.allow_empty === 'true',
			req.query.allowed_categories ? (req.query.allowed_categories as string).split(',') : [],
			req.query.blacklisted_achievements ? (req.query.blacklisted_achievements as string).split(',').map(Number) : []
		);
		const query = generateQuery(filter);
		const achievements = await collections.achievements?.find(query).toArray() as Achievement[];
		res.status(200).json(achievements);
	} catch (error) {
		res.status(500).json({ message: 'An error occurred while fetching achievements.', error: error instanceof Error ? error.message : 'Unknown error' });
	}
});

app.get('/achievements/random', async (req: Request, res: Response) => {
	try{
		const filter = new Filter(
			req.query.allow_empty === 'true',
			req.query.allowed_categories ? (req.query.allowed_categories as string).split(',') : [],
			req.query.blacklisted_achievements ? (req.query.blacklisted_achievements as string).split(',').map(Number) : []
		);
		const query = generateQuery(filter);
		const achievements = await collections.achievements?.find(query).toArray() as Achievement[];

		let random_achievement = achievements.length > 0 ? achievements[getRandomInt(0, achievements.length - 1)] : null;

		res.status(200).json(random_achievement);
	} catch (error) {
		res.status(500).json({ message: 'An error occurred while fetching achievements.', error: error instanceof Error ? error.message : 'Unknown error' });
	}
});

app.get('/achievements/:id', async (req: Request, res: Response) => {
	try{
		const achievement_id = Number(req.params.id);
		const achievement = await collections.achievements?.findOne({id: achievement_id}) as Achievement;
		res.status(200).json(achievement);
	} catch (error) {
		res.status(500).json({ message: 'An error occurred while fetching achievements.', error: error instanceof Error ? error.message : 'Unknown error' });
	}
});

app.listen(PORT, () => {
	console.log(`[server]: Server is running at http://localhost:${PORT}`);
	connectToDatabase()
		.then(() => {
			console.log("Connected to database successfully.");
		})
		.catch((error) => {
			console.error("Failed to connect to database:", error instanceof Error ? error.message : error);
			process.exit(1); // Exit the application if the database connection fails
		});
});

function generateQuery(filter: Filter) {
	let query: any = {};

	if (!filter.allow_empty) {
		query.name = { $nin: ["None", ""] };
	}
	if (filter.allowed_categories.length > 0) {
		query.category = { $in: filter.allowed_categories };
	}
	if (filter.blacklisted_achievements.length > 0) {
		query.id = { $nin: filter.blacklisted_achievements };
	}
	return query;
}

function getRandomInt(min: number, max: number): number {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
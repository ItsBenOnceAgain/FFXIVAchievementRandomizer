// External Dependencies
import * as mongoDB from "mongodb";
import * as dotenv from "dotenv";

dotenv.config();

// Global Variables
export const collections: { achievements?: mongoDB.Collection, users?: mongoDB.Collection } = {};

const db_connection_string: string = process.env.DB_CONN_STRING || "";
const db_name: string = process.env.DB_NAME || "";

// Collections
const achievement_collection_name: string = 	"achievements";
const users_collection_name: string = 			"users";

// Initialize Connection
export async function connectToDatabase () {

	const client: mongoDB.MongoClient = new mongoDB.MongoClient(db_connection_string);   
	await client.connect();
	const db: mongoDB.Db = client.db(db_name);
	const achievementCollection: mongoDB.Collection = db.collection(achievement_collection_name);
	const usersCollection: mongoDB.Collection = db.collection(users_collection_name);
	collections.achievements = achievementCollection;
	collections.users = usersCollection;
}
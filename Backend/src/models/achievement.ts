import { ObjectId } from "mongodb";
import Title from "./title";

export default class Achievement {
    constructor(
        public _id?: ObjectId,
        public id: number = 0,
        public name: string = "",
        public description: string = "",
        public category: string = "",
        public hide_achievement: boolean = false,
        public points: number = 0,
        public icon_path: string = "",
        public item_reward: string = "",
        public item_icon_path: string = "",
        public title: Title = new Title()
    ) {}
}
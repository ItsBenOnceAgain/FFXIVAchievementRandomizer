export class Achievement {
    id: number = 0;
    name: string = "";
    description: string = "";
    icon_path: string = "";
    category: string = "";
    hide_achievement: boolean = false;
    item_reward: string = "";
    title: Title = new Title();
}

export class Title {
    feminine_title: string = "";
    masculine_title: string = "";
    is_prefix: boolean = false;
}
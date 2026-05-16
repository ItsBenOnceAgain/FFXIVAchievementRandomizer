export default class Filter {
    constructor(
        public allow_empty: boolean = false,
        public allowed_categories: string[] = [],
        public blacklisted_achievements: number[] = []
    ) {}
}
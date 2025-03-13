import { GraphService } from './graph.service';
export declare class GraphController {
    private readonly graphService;
    constructor(graphService: GraphService);
    fetchGraph(): Promise<any>;
}

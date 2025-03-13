import { Injectable } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class GraphService {
    private fastApiBaseUrl = 'http://localhost:8000';

    async getGraphData(){
        try{
            const response = await axios.get(`${this.fastApiBaseUrl}/getgraph`);
            return response.data;
        } catch (error) {
            throw new Error('Failed to fetch graph data');
        }
    }
}

import axios from "axios";

const API_BASE_URL = "http://localhost:3000";

export const fetchGraphData = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/graph`);
        return response.data;
    } catch (error) {
        console.error("Error fetching graph data:", error);
        return null;
    }
};  
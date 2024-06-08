import { EventTag } from "./eventTag.models";
import { EventType } from "./eventType.models";

export interface Event {
    id?: number;
    title: string;
    description: string;
    eventType: { id: number, name: string };
    eventTag: { id: number, description: string };
    link: string;
    startDate: Date;
    endDate: Date;
    likes: number;
    location: { id: number, description: string }
}
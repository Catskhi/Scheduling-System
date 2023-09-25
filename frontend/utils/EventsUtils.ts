import axios from "axios"

export interface eventData {
    id: number
    title: string
    address: string
    technical: number
    description: string
    date: string
    start_time: string
    end_time: string
}

export interface technicalData {
    id: number
    name: string
}

export const getAllEvents = async () => {
    let allEvents: eventData[] = []
    await axios.get(getServerUrl() + '/events/')
    .then((response) => {
        allEvents = response.data
        console.log(allEvents)
    })
    .catch((error) => {
        console.log(error.response.data)
    })

    return allEvents
}

export const getEventData = async (eventId: number) => {
    let currentEvent: eventData | undefined
    await axios.get(getServerUrl() + '/events/' + eventId + '/')
    .then((response) => {
        currentEvent = response.data
        console.log(currentEvent)
    })
    .catch((error) => {
        console.log(error.response.data)
    })

    return currentEvent
}

export const getAllTechnicals = async () => {
    let allTechnicals: technicalData[] = []
    await axios.get(getServerUrl() + '/technicals/')
    .then((response) => {
        allTechnicals = response.data
    })
    .catch((error) => {
        console.log(error.response.data)
    })
    return allTechnicals
}
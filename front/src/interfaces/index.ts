export interface Listing {
    id: number,
    place_id: number,
    price: number,
    area: number,
    room_count: number,
    seen_at: Date
}

export interface ListingHistory extends Listing {
    history: Array<{ date: Date, price: number }>
}
import { Listing } from 'interfaces';
import { mockedData } from '../Listing/Listing.fixture';

const Listings = (): JSX.Element => {

    const data: Array<any> = mockedData;

    const sortByDate = ( arr: Array<any> ): Array<any> => {
        return [];
    };
    const sortByRoomCount = ( arr: Array<any>, order: 'ASC' | 'DESC' = 'DESC' ): Array<any> => {
        return arr.sort( ( a, b ) => {
            if ( order === 'DESC' ) {
                return new Date( a.seen_at ) > new Date( b.seen_at ) ? 1 : -1;
            }
            return new Date( a.seen_at ) < new Date( b.seen_at ) ? 1 : -1;
        } );
    };
    return (
        <>
            <h1>Welcome to the listing page</h1>

        </>
    );
}

export default Listings;
import ListingForm from '../../components/ListingForm';
import axios, { AxiosResponse } from 'axios';
import { useEffect, useState } from 'react';
import ListingCard from '../../components/ListingCard/ListingCard';
import { ListingInterface } from '../../components/ListingCard/ListingCard';

const Listings = () => {
    const [listings, updateListings]: Array<any> = useState( [] );

    useEffect( () => {
        axios.get( 'https://stoplight.io/mocks/testtmptesttmp/testtmptesttmp/125999361/listings' )
            .then( ( response: AxiosResponse<Array<ListingInterface>> ) => {
                console.log( response.data );
                updateListings( response.data );
            } )
            .catch( ( error ) => {
                console.error( error );
            } );
    }, [] ); 

    return (
        <main className="container">
            <h1 className="title">Listings</h1>
            <section>
                <h2>Add a listing</h2>
                <ListingForm />
            </section>
            <section className="card-container">
                {
                    listings.map( ( listing: ListingInterface ) => {
                        return ( <ListingCard key={listing.id} listing={listing} /> );
                    } )
                }
            </section>
        </main>
  );
};

export default Listings;

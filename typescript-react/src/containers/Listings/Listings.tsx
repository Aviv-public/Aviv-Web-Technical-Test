import { useEffect, useState } from 'react';

import ListingForm from '../../components/ListingForm';
import ListingDetails from '../../components/ListingDetails';
import { Listing } from '../../types/Listing';

import { getListings } from '../../services/Api';

const Listings = () => {
  const [listings, setListings] = useState<Listing[]>([]);

  const onUpdateListings = (newListing: Listing) => {
    setListings([...listings, newListing]);
  };

  useEffect(() => {
    getListings()
      .then((res) => setListings(res.data))
      .catch((err) => err);
  }, []);

  return (
    <main className="container">
      <h1 className="title">Main Listings page</h1>

      <section className="card-container">
        <h2>Add a listing</h2>

        <ListingForm
          onUpdateListings={(newListing: Listing) =>
            onUpdateListings(newListing)
          }
        />
      </section>

      <section className="card-container">
        <h2>Listings</h2>

        {listings?.length > 0 &&
          listings.map(
            ({
              building_type,
              description,
              id,
              latest_price_eur,
              postal_address,
              rooms_count,
              surface_area_m2,
              updated_date,
            }) => {
              return (
                <ListingDetails
                  key={id}
                  buildingType={building_type}
                  description={description}
                  id={id}
                  latestPrice={latest_price_eur}
                  postalAddress={postal_address}
                  roomsCount={rooms_count}
                  surfaceArea={surface_area_m2}
                  updatedDate={updated_date}
                />
              );
            },
          )}
      </section>
    </main>
  );
};

export default Listings;

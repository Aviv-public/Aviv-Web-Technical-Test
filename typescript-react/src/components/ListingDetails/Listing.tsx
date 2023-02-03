import { PostalAddress } from '../../types/Listing';

import { getFormattedDate } from '../../helpers/Date/Date';

interface ListingDetailsProps {
  buildingType: string;
  description: string;
  id: number;
  latestPrice: number;
  postalAddress: PostalAddress;
  roomsCount: number;
  surfaceArea: number;
  updatedDate: Date;
}

const ListingDetails = ({
  buildingType,
  description,
  latestPrice,
  postalAddress,
  id,
  roomsCount,
  surfaceArea,
  updatedDate,
}: ListingDetailsProps) => {
  return (
    <div className="listing-card">
      <span className="listing-card__price">
        {latestPrice.toLocaleString()} &euro;
      </span>

      <dl className="listing-card__properties">
        <dt className="listing-card__properties-item">{buildingType}</dt>
        <dt className="listing-card__properties-item">
          {surfaceArea}m<sup>2</sup>
        </dt>
        <dt className="listing-card__properties-item">{roomsCount} rooms</dt>
      </dl>

      <section className="listing-card__address">
        <address>
          {postalAddress?.street_address}, {postalAddress?.postal_code},{' '}
          {postalAddress?.city}, {postalAddress?.country}
        </address>
      </section>

      <section className="listing-card__description">
        <h3>Property description: </h3>
        <p>{description || 'No description'}</p>
      </section>

      <a
        href={`http://localhost:5173/${id}/prices`}
        className="listing-card__link"
      >
        See history &rarr;
      </a>

      <p className="listing-card__reference">
        Ref: {id} <br />
        Last update: {getFormattedDate(updatedDate)}
      </p>
    </div>
  );
};

export default ListingDetails;

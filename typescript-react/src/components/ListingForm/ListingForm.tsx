import { ChangeEvent, FormEvent, useState } from 'react';
import { addNewListing } from '../../services/Api';
import { Listing, PostalAddress } from '../../types/Listing';

interface ListingFormProps {
  onUpdateListings: (newListing: Listing) => void;
}

const ListingForm = ({ onUpdateListings }: ListingFormProps) => {
  const initialData = {
    bedrooms_count: 0,
    building_type: '',
    contact_phone_number: '',
    description: '',
    latest_price_eur: 0,
    name: '',
    rooms_count: 0,
    surface_area_m2: 0,
  };

  const initialPostalAddress = {
    city: '',
    country: '',
    postal_code: '',
    street_address: '',
  };

  const [data, setData] =
    useState<
      Omit<Listing, 'created_date' | 'id' | 'postal_address' | 'updated_date'>
    >(initialData);

  const [postalAddress, setPostalAddress] =
    useState<PostalAddress>(initialPostalAddress);

  const handleChangeData = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;
    setData({ ...data, [name]: value });
  };

  const handleChangePostalAddress = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setPostalAddress({ ...postalAddress, [name]: value });
  };

  const onSubmit = (e: FormEvent) => {
    e.preventDefault();

    const payload = {
      ...data,
      postal_address: postalAddress,
    };

    addNewListing(payload)
      .then((res) => onUpdateListings(res.data))
      .catch((err) => err);
  };

  return (
    <form className="listing-form" onSubmit={onSubmit}>
      <div className="listing-form__card">
        <div className="listing-form__input-group">
          <label htmlFor="latest_price_eur">Name</label>
          <input
            type="string"
            name="name"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.name}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="latest_price_eur">Bedrooms count</label>
          <input
            type="number"
            name="bedrooms_count"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.bedrooms_count}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="street_address">Street address</label>
          <input
            type="text"
            name="street_address"
            className="listing-form__input-text"
            onChange={handleChangePostalAddress}
            value={postalAddress.street_address}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="city">City</label>
          <input
            type="string"
            name="city"
            className="listing-form__input-text"
            onChange={handleChangePostalAddress}
            value={postalAddress.city}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="contact_phone_number">Country</label>
          <input
            type="string"
            name="country"
            className="listing-form__input-text"
            onChange={handleChangePostalAddress}
            value={postalAddress.country}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="postal_code">Postal code</label>
          <input
            type="string"
            name="postal_code"
            className="listing-form__input-text"
            onChange={handleChangePostalAddress}
            value={postalAddress.postal_code}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="contact_phone_number">Contact Phone Number</label>
          <input
            type="string"
            name="contact_phone_number"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.contact_phone_number}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="contact_phone_number">Description</label>
          <input
            type="string"
            name="description"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.description}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="latest_price_eur">Price</label>
          <input
            type="number"
            name="latest_price_eur"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.latest_price_eur}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="postal_code">Rooms Count</label>
          <input
            type="number"
            name="rooms_count"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.rooms_count}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="surface_area_m2">Surface area</label>
          <input
            type="number"
            name="surface_area_m2"
            className="listing-form__input-text"
            onChange={handleChangeData}
            value={data.surface_area_m2}
          />
        </div>

        <div className="listing-form__input-group">
          <label htmlFor="building_type">Building type:</label>
          <select
            name="building_type"
            className="listing-form__select"
            onChange={handleChangeData}
            value={data.building_type}
          >
            <option value="STUDIO">Studio</option>
            <option value="APARTMENT">Apartment</option>
            <option value="HOUSE">House</option>
          </select>
        </div>

        <button type="submit" className="listing-form__button--submit">
          Create
        </button>
      </div>
    </form>
  );
};

export default ListingForm;

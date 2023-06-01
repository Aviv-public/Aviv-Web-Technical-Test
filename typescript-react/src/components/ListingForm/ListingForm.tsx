import { ChangeEvent, FormEvent, useReducer } from 'react';

import styles from './listing-form.module.scss';

import { formReducer, initialState } from '@/reducers/formReducer';
import { FormState } from '@/types/form';
import { createListing } from '@/utils/requests';

const ListingForm = () => {
  const [formData, dispatch] = useReducer(formReducer, initialState);

  const submit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    createListing(formData);
    dispatch({ type: 'RESET' });
  };

  const handleInputChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) => {
    const { name, value } = e.target;
    dispatch({ type: 'CHANGE', field: name as keyof FormState, value });
  };

  return (
    <form className={styles['listing-form']} onSubmit={submit}>
      <div className={styles['listing-form__card']}>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="name">
            <span className={styles['listing-form__required-field']}>*</span>
            Name:
          </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="contact_phone_number">
            <span className={styles['listing-form__required-field']}>*</span>
            Phone number:
          </label>
          <input
            type="text"
            name="contact_phone_number"
            value={formData.contact_phone_number}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="city">
            <span className={styles['listing-form__required-field']}>*</span>
            City:
          </label>
          <input
            type="text"
            name="city"
            value={formData.postal_address.city}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="country">
            <span className={styles['listing-form__required-field']}>*</span>
            Country:
          </label>
          <input
            type="text"
            name="country"
            value={formData.postal_address.country}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="postal_code">
            <span className={styles['listing-form__required-field']}>*</span>
            Postal Code:
          </label>
          <input
            type="text"
            name="postal_code"
            value={formData.postal_address.postal_code}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="street_address">
            <span className={styles['listing-form__required-field']}>*</span>
            Street address:
          </label>
          <input
            type="text"
            name="street_address"
            value={formData.postal_address.street_address}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="bedrooms_count">
            <span className={styles['listing-form__required-field']}>*</span>
            Bedrooms:
          </label>
          <input
            type="number"
            name="bedrooms_count"
            value={formData.bedrooms_count}
            className={styles['listing-form__input-number']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="rooms_count">
            <span className={styles['listing-form__required-field']}>*</span>
            Rooms:
          </label>
          <input
            type="number"
            name="rooms_count"
            value={formData.rooms_count}
            className={styles['listing-form__input-number']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="latest_price_eur">
            <span className={styles['listing-form__required-field']}>*</span>
            Price:
          </label>
          <input
            type="text"
            name="latest_price_eur"
            value={formData.latest_price_eur}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="surface_area_m2">
            <span className={styles['listing-form__required-field']}>*</span>
            Area:
          </label>
          <input
            type="text"
            name="surface_area_m2"
            value={formData.surface_area_m2}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="description">
            <span className={styles['listing-form__required-field']}>*</span>
            Description:
          </label>
          <input
            type="text"
            name="description"
            value={formData.description}
            className={styles['listing-form__input-text']}
            onChange={handleInputChange}
          />
        </div>
        <div className={styles['listing-form__input-group']}>
          <label htmlFor="building_type">
            <span className={styles['listing-form__required-field']}>*</span>
            Building type:
          </label>
          <br />
          <select
            name="building_type"
            value={formData.building_type}
            className={styles['listing-form__select']}
            onChange={handleInputChange}
          >
            <option value="STUDIO">Studio</option>
            <option value="APARTMENT">Apartment</option>
            <option value="HOUSE">House</option>
          </select>
        </div>
        <button
          type="submit"
          className={styles['listing-form__button--submit']}
        >
          Create
        </button>
      </div>
    </form>
  );
};

export default ListingForm;

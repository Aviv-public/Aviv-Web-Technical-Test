const ListingForm = () => {
  const submit = () => null;

  return (
    <form className="listing-form" onSubmit={submit}>
      <div className="listing-form__card">
        <div className="listing-form__input-group">
          <label htmlFor="latest_price_eur">Price:</label>
          <input
            type="text"
            name="latest_price_eur"
            className="listing-form__input-text"
          />
        </div>
        <div className="listing-form__input-group">
          <label htmlFor="surface_area_m2">Area:</label>
          <input
            type="text"
            name="surface_area_m2"
            className="listing-form__input-text"
          />
        </div>
        <div className="listing-form__input-group">
          <label htmlFor="street_address">Street address:</label>
          <input
            type="text"
            name="street_address"
            className="listing-form__input-text"
          />
        </div>
        <div className="listing-form__input-group">
          <label htmlFor="building_type">Building type:</label>
          <select name="building_type" className="listing-form__select">
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

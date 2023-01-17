const ListingForm = () => {
    const submit = () => { }

    return (
        <form className="listing-form" onSubmit={submit}>
            <div className="listing-form__card">
                <div className="listing-form__input-group">
                    <label htmlFor="price">Price:</label>
                    <input type="text" name="price" className="listing-form__input-text" />
                </div>
                <div className="listing-form__input-group">
                    <label htmlFor="price">Area:</label>
                    <input type="text" name="price" className="listing-form__input-text" />
                </div>
                <div className="listing-form__input-group">
                    <label htmlFor="price">Street address:</label>
                    <input type="text" name="Street_address" className="listing-form__input-text" />
                </div>
                <div className="listing-form__input-group">
                    <label htmlFor="building_type">Building type:</label>
                    <select name="building_type" className="listing-form__select">
                        <option value="STUDIO">Studio</option>
                        <option value="APARTMENT">Appartement</option>
                        <option value="HOUSE">Maison</option>
                    </select>
                </div>
                <button type="submit" className="listing-form__button--submit" >Send</button>
            </div>
        </form >
    );
};

export default ListingForm;

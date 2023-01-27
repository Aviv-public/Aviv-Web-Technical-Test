import ListingForm from '../../components/ListingForm';

const Listings = () => {
  return (
    <main className="container">
      <h1 className="title">Main Listings page</h1>

      <section className="card-container">
        <h2>Add a listing</h2>
        <ListingForm />
      </section>
      <section className="card-container">
        <h2>Listings</h2>
        <article className="listing-card">
          <span className="listing-card__price">320 000 &euro;</span>
          <dl className="listing-card__properties">
            <dt className="listing-card__properties-item">Studio</dt>
            <dt className="listing-card__properties-item">
              74m<sup>2</sup>
            </dt>
            <dt className="listing-card__properties-item">3 rooms</dt>
          </dl>
          <section className="listing-card__address">
            <address>48, boulevard des capucins, 10294, Paris</address>
          </section>
          <section className="listing-card__description">
            <h3>Property description: </h3>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
              commodo, arcu eu varius dapibus, lacus velit posuere tellus, nec
              convallis sem velit ut leo. Maecenas maximus volutpat felis.
            </p>
          </section>
          <a className="listing-card__link">See history &rarr;</a>
          <p className="listing-card__reference">
            Ref: 123456 <br />
            Last update: 31/12/2021
          </p>
        </article>
      </section>
    </main>
  );
};

export default Listings;

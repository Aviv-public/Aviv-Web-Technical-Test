const Listings = () => {
  return (
    <div className="container">
      <h1 className="title">Welcome to the listing page</h1>
      <div className="card">
        <input className="input" type="checkbox" />
        <div>
          <div className="top-block">
            <h2 className="price">295 000 €</h2>
            <span className="read">✓ Vu à 17h45</span>
          </div>

          <p className="place">T1 • Paris 17e</p>
          <p className="reference"> ref 1969719989</p>
          <span className="see-more">Voir l'annonce →</span>
        </div>
      </div>

      <div className="card card-selected" />
    </div>
  );
};

export default Listings;

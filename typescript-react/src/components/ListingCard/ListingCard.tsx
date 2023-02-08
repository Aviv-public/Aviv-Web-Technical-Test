import styles from './listing-card.module.scss';

const ListingCard = () => {
  return (
    <article className={styles['listing-card']}>
      <span className={styles['listing-card__price']}>320 000 &euro;</span>
      <dl className={styles['listing-card__properties']}>
        <dt className={styles['listing-card__properties-item']}>Studio</dt>
        <dt className={styles['listing-card__properties-item']}>
          74m<sup>2</sup>
        </dt>
        <dt className={styles['listing-card__properties-item']}>3 rooms</dt>
      </dl>
      <section className={styles['listing-card__address']}>
        <address>48, boulevard des capucins, 10294, Paris</address>
      </section>
      <section className={styles['listing-card__description']}>
        <h3>Property description: </h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
          commodo, arcu eu varius dapibus, lacus velit posuere tellus, nec
          convallis sem velit ut leo. Maecenas maximus volutpat felis.
        </p>
      </section>
      <div className={styles['listing-card__footer']}>
        <p className={styles['listing-card__reference']}>
          Ref: 123456 <br />
          Last update: 31/12/2021
        </p>
        <a href="/" className={styles['listing-card__link']}>
          See history &rarr;
        </a>
      </div>
    </article>
  );
};

export default ListingCard;

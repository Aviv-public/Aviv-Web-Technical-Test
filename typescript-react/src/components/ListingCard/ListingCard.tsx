import styles from './listing-card.module.scss';

const ListingCard = () => {
  return (
    <article className={styles['listing-card']}>
      <span className={styles['listing-card__price']}>320 000 &euro;</span>
      <ul className={styles['listing-card__properties']}>
        <li className={styles['listing-card__properties-item']}>Studio</li>
        <li className={styles['listing-card__properties-item']}>
          74m<sup>2</sup>
        </li>
        <li className={styles['listing-card__properties-item']}>3 rooms</li>
      </ul>
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
          Last update: 2021/12/31
        </p>
        <a href="/" className={styles['listing-card__link']}>
          See history &rarr;
        </a>
      </div>
    </article>
  );
};

export default ListingCard;

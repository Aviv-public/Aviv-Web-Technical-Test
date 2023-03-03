import PricesHistoryCard from '@components/PriceHistoryCard';
import styles from './prices-history.module.scss';

const PricesHistory = () => {
  return (
    <div className={styles['container']}>
      <h1>Prices History</h1>
      <PricesHistoryCard />

      <a href="/" className={styles['link']}>
        &larr; Back Home
      </a>
    </div>
  );
};
export default PricesHistory;

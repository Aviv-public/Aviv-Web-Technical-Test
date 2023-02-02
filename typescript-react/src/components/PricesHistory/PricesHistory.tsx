import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { PriceHistory } from '../../types/Listing';
import { getFormattedDate } from '../../helpers/Date/Date';
import { getPricesHistory } from '../../services/Api';

const PricesHistory = () => {
  const { listingId } = useParams();

  const [pricesHistory, setPricesHistory] = useState<PriceHistory[]>([]);

  useEffect(() => {
    listingId &&
      getPricesHistory(listingId)
        .then((res) => setPricesHistory(res.data))
        .catch((err) => err);
  }, [listingId]);

  return (
    <table>
      <caption>Prices History</caption>
      <tbody>
        <tr>
          <th scope="col">Date</th>
          <th scope="col">Price (eur)</th>
        </tr>

        {pricesHistory?.length > 0 &&
          pricesHistory.map(({ created_date, price_eur }, index) => {
            return (
              <tr key={index}>
                <td>{getFormattedDate(created_date)}</td>
                <td>{price_eur.toLocaleString()} €</td>
              </tr>
            );
          })}
      </tbody>
    </table>
  );
};
export default PricesHistory;

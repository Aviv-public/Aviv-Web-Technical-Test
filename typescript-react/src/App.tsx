import Header from './components/Header/Header';
import Listings from './containers/Listings/Listings';
import PriceHistory from './components/PricesHistory';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const App = () => (
  <>
    <Header />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Listings />} />
        <Route path=":listingId/prices" element={<PriceHistory />} />
      </Routes>
    </BrowserRouter>
  </>
);

export default App;

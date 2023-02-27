import Header from './components/Header/Header';
import Listings from './containers/Listings/Listings';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

const App = () => (
  <>
    <Header />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Listings />} />
      </Routes>
    </BrowserRouter>
  </>
);

export default App;

import Header from './components/Header/Header';
import Listings from './containers/Listings/Listings';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <Header />
      <BrowserRouter>
        <Routes>
                  <Route path="/" element={<Listings />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;

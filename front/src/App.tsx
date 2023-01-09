import Header from './components/Header/Header';
import Listings from './containers/Listings/Listings';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Listing from './containers/Listing/Listing';
function App() {
    return <>
        <Header />
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Listings />} />
                <Route path="/:listingId" element={<Listing />} />
            </Routes>
        </BrowserRouter>
    </>;
}

export default App;

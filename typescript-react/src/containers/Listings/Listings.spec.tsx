import { render, screen } from '@testing-library/react';
import Listings from './Listings';

describe( '<Listings /> test suite', () => {
    it( 'Should render the <Listings /> component', () => {
        render( <Listings /> );
    } );
} );

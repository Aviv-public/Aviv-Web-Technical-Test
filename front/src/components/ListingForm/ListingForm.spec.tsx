import { render, screen } from '@testing-library/react';

import ListingForm from '.';

describe( '<ListingForm />', () => {
    it( 'Should render the header component', () => {
        render( <ListingForm /> );
    } );
} );

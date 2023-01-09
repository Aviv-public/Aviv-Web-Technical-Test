import { render, screen } from '@testing-library/react';

import Header from '.';

describe( '<Header />', () => {
    it( 'Should render the header component', () => {
        render( <Header /> );
    } );
} );

import { render, screen } from '@testing-library/react';

import Header from '.';

describe( '<Header />', () => {
    it( 'should render a top bar with logo, messagesCounter and realtor select', () => {
        render( <Header /> );

        expect( screen.getByTestId( 'select-realtor' ) ).toBeInTheDocument();
    } );
} );

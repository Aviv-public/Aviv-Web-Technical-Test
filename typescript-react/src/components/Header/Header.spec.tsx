import { render } from '@testing-library/react';
import { describe, it } from 'vitest';

import Header from '.';

describe('<Header />', () => {
  it('Should render the header component', () => {
    render(<Header />);
  });
});

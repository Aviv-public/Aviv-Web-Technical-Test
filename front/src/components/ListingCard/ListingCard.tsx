import { compile } from 'sass';

export interface ListingInterface {
    id: number,
    name: string,
    postal_address: {
        street_address: string,
        postal_code: string,
        city: string,
        country: string
    },
    description: string,
    building_type: string,
    price: {
        price_eur: number,
        created_date: string
    },
    surface_area_m2: number,
    rooms_count: number,
    bedrooms_count: number,
    contact_phone_number: string,
    created_date: Date,
    updated_date: Date
}

export interface Props { };

const ListingCard = ( props: { listing: ListingInterface } ) => {
    const listing: ListingInterface = props.listing;

    const formatDate = ( date: Date ): string => {
        let d = new Date( date );
        const day = d.getDate().toString().padStart( 2, '0' );
        const month = ( d.getMonth() + 1 ).toString().padStart( 2, '0' );
        const year = d.getFullYear();
        const hour = d.getHours().toString().padStart( 2, '0' );
        const minute = d.getMinutes().toString().padStart( 2, '0' );
        return `${ day }/${ month }/${ year }`;
    }

    const splitNumber = ( num: number ): string => {
        return num.toString().replace( /\B(?=(\d{3})+(?!\d))/g, " " );
    }

    const buildingTypeLabel = ( type: string ) => {
        switch ( type ) {
            case 'STUDIO':
                return 'Studio';
            case 'APARTMENT':
                return 'Apartment';
            case 'HOUSE':
                return 'House';
        }
    };
    return (
        <article className="listing-card">
            <span className="listing-card__price">{splitNumber( listing.price.price_eur )} &euro;</span>
            <dl className="listing-card__properties">
                <dt className="listing-card__properties-item">{buildingTypeLabel( listing.building_type )}</dt>
                <dt className="listing-card__properties-item">74m<sup>2</sup></dt>
                <dt className="listing-card__properties-item">{listing.rooms_count} rooms</dt>
            </dl>
            <section className="listing-card__address">
                <address>{`${ listing.postal_address.street_address }, ${ listing.postal_address.postal_code }, ${ listing.postal_address.city }`}</address>
            </section>
            <section className="listing-card__description">
                <h3>Property description: </h3>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Nullam commodo, arcu eu varius dapibus, lacus velit posuere tellus,
                    nec convallis sem velit ut leo. Maecenas maximus volutpat felis.
                    {/* {listing.description} */}
                </p>
            </section>
            <a className="listing-card__link" href={'/' + listing.id + '/history'}>See history &rarr;</a>
            <p className="listing-card__reference">Ref: {listing.id}</p>

        </article>

    );
}

export default ListingCard;

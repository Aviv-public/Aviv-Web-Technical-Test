import styles from './header.module.scss';

const Header = () => {
  return (
    <header className={styles['header']}>
      <img src="/assets/logo-aviv.svg" alt="logo Aviv" />
    </header>
  );
};

export default Header;

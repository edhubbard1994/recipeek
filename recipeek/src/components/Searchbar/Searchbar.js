import React from 'react';
import PropTypes from 'prop-types';
import styles from './Searchbar.module.css';

const Searchbar = (props) => {
    let { label, onClick, searchInput, onChange } = props;

    return (
        <div className={styles.searchbar}>
            <input
                className={styles.searchbarInputField}
                type="text"
                placeholder={label}
                value={searchInput}
                onChange={onChange}
            />
            <button onClick={onClick} className={styles.searchbarButton}>
                Search
            </button>
        </div>
    );
};

Searchbar.propTypes = {
    label: PropTypes.string,
    onClick: PropTypes.func.isRequired,
    searchInput: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
};

Searchbar.defaultProps = {
    label: 'Search',
};

export default Searchbar;

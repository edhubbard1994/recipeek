import React from 'react';
import PropTypes from 'prop-types';
import styles from './SearchResultCard.module.css';

const SearchResultCard = (props) => {
    let { recipeName, cuisine, diet, recipeURL, recipeImageURL } = props;

    return (
      <div onClick={() => {window.open(recipeURL)}} className={styles.card}>
        <img
          src={recipeImageURL}
          alt={recipeName}
          className={styles.recipeImage}
        />
        <h1 className={styles.name}>
          {recipeName}
        </h1>
        <div className={styles.separator}/>
        <div className={styles.labelBoxCuisine}>
          <h1 className={styles.label}>Cuisine</h1>
        </div>
        <h1 className={styles.cuisineText}>
          {cuisine}
        </h1>
        <div className={styles.labelBoxDiet}>
          <h1 className={styles.label}>Diet</h1>
        </div>
        <h1 className={styles.dietText}>
          {diet}
        </h1>
      </div>
    );
};

SearchResultCard.propTypes = {
  recipeName: PropTypes.string.isRequired,
  cuisine: PropTypes.string,
  diet: PropTypes.string,
  // onClick: PropTypes.func.isRequired,
  recipeURL: PropTypes.string.isRequired,
  recipeImageURL: PropTypes.string,
};

SearchResultCard.defaultProps = {
  cuisine: 'unknown',
  diet: 'unknown',
  recipeImageURL: 'https://image.flaticon.com/icons/svg/857/857681.svg',
};

export default SearchResultCard;

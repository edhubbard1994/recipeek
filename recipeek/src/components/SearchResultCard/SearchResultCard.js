import React from 'react';
import PropTypes from 'prop-types';
import styles from './SearchResultCard.module.css';

const SearchResultCard = (props) => {
    let { recipeName, cuisine, diet, calories, recipeURL, recipeImageURL } = props;

    let MAX_LENGTH = 40;

    if (recipeName.length >= MAX_LENGTH) {
      var name = recipeName.substr(0, MAX_LENGTH) + "\u2026";
    }
    else {
      var name = recipeName;
    }

    return (
      <div onClick={() => {window.open(recipeURL)}} className={styles.card}>
        <img
          src={recipeImageURL}
          alt={recipeName}
          className={styles.recipeImage}
        />
        <h1 className={styles.name}>
          {name}
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
        <div className={styles.labelBoxCal}>
          <h1 className={styles.label}>Calories</h1>
        </div>
        <h1 className={styles.calText}>
          {calories}
        </h1>
      </div>
    );
};

SearchResultCard.propTypes = {
  recipeName: PropTypes.string.isRequired,
  cuisine: PropTypes.string,
  diet: PropTypes.string,
  calories: PropTypes.number,
  recipeURL: PropTypes.string.isRequired,
  recipeImageURL: PropTypes.string,
};

SearchResultCard.defaultProps = {
  cuisine: 'unknown',
  diet: 'unknown',
  recipeImageURL: 'https://image.flaticon.com/icons/svg/857/857681.svg',
};

export default SearchResultCard;

import React from 'react';
import PropTypes from 'prop-types';
import styles from './Avatar.module.css';

const Avatar = (props) => {
    let { size, avatarData, alt, onClick } = props;
    let { imageURL, username } = avatarData;

    let dynamicSize = {
        height: size,
        width: size,
        borderRadius: '50%',
    };

    if (imageURL) { //if image url exists, use photo
        return (
            <img
                src={imageURL}
                alt={alt}
                style={dynamicSize}

                className={styles.avatar}
                onClick={onClick}
            />
        );
    } else { //otherwise, use first initial
        let firstInitial = username.slice(0, 1).toUpperCase();
        let letterSize = parseInt(size.replace('px', '')) * 0.5; //uses size of avatar to calc
        let fontSize = `${letterSize}px`;

        return (
            <div className={styles.avatar} style={dynamicSize} onClick={onClick}>
                <h1 style={{ fontSize: fontSize }}>{firstInitial}</h1>
            </div>
        );
    }
};

Avatar.propTypes = {
    size: PropTypes.string,
    alt: PropTypes.string.isRequired,
    onClick: PropTypes.func.isRequired,
    avatarData: PropTypes.shape({
        imageURL: PropTypes.string,
        username: PropTypes.string.isRequired,
    }).isRequired,
};

Avatar.defaultProps = {
    size: '7px',
};

export default Avatar;

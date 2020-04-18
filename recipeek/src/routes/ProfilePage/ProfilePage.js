import React, { Component } from 'react';
import Avatar from '../../components/Avatar';
import styles from './ProfilePage.module.css';

export default class Home extends Component {

    render() {
        return (
            <div className={styles.wrapper}>
              <div className={styles.header}>
                <div className={styles.avatar}>
                  <Avatar
                    size = '10vw'
                    alt = "test image"
                    onClick = {() => {alert('clicked')}}
                    avatarData = {{
                      avatarImageURL: 'https://images.unsplash.com/photo-1543333108-4f3e0f5a7d11?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1336&q=80',
                      username: 'user',
                    }}
                  />
                </div>
                <div className={styles.name}>
                  User Name
                </div>
              </div>
            </div>
        );
    }
}

import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';

export default class Home extends Component {
    render() {
        return (
            <div>
                <h1>Recipeek</h1>
                {/* TODO center searchbar */}
                <Searchbar
                  label = 'Find your feast...'
                  onClick = {() => {alert('Button Clicked')}}
                  searchInput = ''
                  onChange = { () => {alert('onChange')} }
                />
            </div>
        );
    }
}

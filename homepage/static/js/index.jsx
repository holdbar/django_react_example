import React from 'react'
import ReactDOM from 'react-dom'


class Test extends React.Component {
    render() {
        var list = window.props;
        return <div>{list.map(item => <TestChild key={item.pk}  
                        title={item.title} 
                        description={item.description}/> )}</div>;
    }
}

class TestChild extends React.Component {
    render() {
     return <li><b>{this.props.title}</b>: {this.props.description}</li>;
    }
}


ReactDOM.render(
    <Test/>, 
    window.react_mount, 
)
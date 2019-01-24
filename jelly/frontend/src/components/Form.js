import React, { Component } from "react";
import PropTypes from "prop-types";

class Form extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };

  state = {
    name: "",
    version: "",
    era: undefined
  };

  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = e => {
    e.preventDefault();
    const { name, version, era } = this.state;
    const game = { name, version, era };
    const conf = {
      method: "post",
      body: JSON.stringify(game),
      headers: new Headers({ "Content-Type": "application/json" })
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };

  render() {
    const { name, version, era } = this.state;
    return (
      <div className="column">
        <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">Name</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="name"
                onChange={this.handleChange}
                value={name}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Version</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="version"
                onChange={this.handleChange}
                value={version}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Era</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="era"
                onChange={this.handleChange}
                value={era}
                required
              />
            </div>
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Send message
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default Form;
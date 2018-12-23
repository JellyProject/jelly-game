import React, { Component } from 'react';
import './App.css';

class MainGrid extends Component {
    render() {
        return (
            <div className="main-grid">
                <MainHeader/>
                <MenuGrid/>
            </div>
        );
    }
}

class MainHeader extends Component {
    render() {
        return (
            <div className="main-header">
                <BoxHover text="MENU 1" />
                <BoxHover text="MENU 2" />
            </div>
        );
    }
}

class MenuGrid extends Component {
    render() {
        return (
            <div className="menu-grid">
                <MenuDisplay/>
                <MenuMonitor/>
                <MenuFooter/>
            </div>
        );
    }
}

class MenuDisplay extends Component {
    render() {
        return(
            <div className="menu-display hover">
                DISPLAY
            </div>
        );
    }
}

class MenuMonitor extends Component {
    render() {
        return(
            <div className="menu-monitor">
                <MenuMonitorStats text="STATS 1"/>
                <MenuMonitorStats text="STATS 2"/>
                <MenuMonitorStats text="STATS 3"/>
                <MenuMonitorStats text="STATS 4"/>
            </div>
        );
    }
}

class MenuMonitorStats extends Component {
    render() {
        return(
            <div className="menu-monitor-stats hover">
                {this.props.text}
            </div>
        );
    }
}

class MenuFooter extends Component {
    render() {
        return(
            <div className="menu-footer">
                <MenuFooterTabs/>
                <MenuFooterActions/>
            </div>
        );
    }
}

class MenuFooterTabs extends Component {
    render() {
        return(
            <div className="menu-footer-tabs hover">
                <BoxHover text="TAB 1"/>
                <BoxHover text="TAB 2"/>
                <BoxHover text="TAB 3"/>
            </div>
        );
    }
}
class MenuFooterActions extends Component {
    render() {

        let actionsWidth = window.innerWidth / 10.3 * 0.8;
        let actionsGap = window.innerWidth / 11 * 0.2;
        let style = {
            display: "grid",
            gridTemplateColumns: "repeat(10, " + actionsWidth + "px)",
            gridAutoFlow: "row",
            gridAutoRows: actionsWidth,
            gridRow: "2",
            gridGap: actionsGap,
            paddingTop: "1em",
            paddingBottom: "1em",
            paddingLeft: "1em",
            paddingRight: "1em",
            border: "0.01em solid #fff435",
            height: "7em",
            overflowY: "auto"
        }

        return(
            <div style={style}>
                <div className="action img-building"></div>
                <div className="action img-chimneys"></div>
                <div className="action img-factory"></div>
                <div className="action img-building"></div>
                <div className="action img-chimneys"></div>
                <div className="action img-factory"></div>
                <div className="action img-building"></div>
                <div className="action img-chimneys"></div>
                <div className="action img-factory"></div>
                <div className="action img-building"></div>
                <div className="action img-chimneys"></div>
                <div className="action img-factory"></div>
                <div className="action img-building"></div>
                <div className="action img-chimneys"></div>
                <div className="action img-factory"></div>
            </div>
        );
    }
}

class BoxHover extends Component {
    render() {
        return(
            <div className="box hover">
                {this.props.text}
            </div>
        );
    }
}

export default MainGrid;
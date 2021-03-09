import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Route} from 'react-router-dom'
import Footer from './components/Footer';
import Header from './components/Header';
import HomeScreen from './screens/HomeScreen';
import WalkerListScreen from './screens/WalkerListScreen';
import LoginScreen from './screens/LoginScreen';

function App() {
    return (
        <Router>
            <Header/>
            <main className="py-3">
                <Container>
                    <Route path='/' component={HomeScreen} exact />
                    <Route path='/login' component={LoginScreen} />
                    <Route path='/walkers' component={WalkerListScreen} />
                </Container>  
            </main>
            <Footer/>
        </Router>
    );
}

export default App;

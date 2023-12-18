import { BrowserRouter, Route, Routes } from "react-router-dom";
import LoginPage from "./components/UI/pages/LoginPage";
import MaintPage from "./components/UI/pages/MainPage";
import ProtectedRouter from "./components/hoc/ProtectedRoute";
import { useAuth } from "./hooks/useAuth";
import { AuthContext } from "./context/AuthContext";


export default function App() {
  const { user, login, logout, setUser } = useAuth();

  return (
    <div className="App">
      <AuthContext.Provider value={{ user, setUser }}>
        <BrowserRouter>
          <Routes>
            <Route element={<ProtectedRouter />}>
              <Route path="/" element={<MaintPage />} />
            </Route>
            <Route path="login" element={<LoginPage />} />
          </Routes>
        </BrowserRouter>
      </AuthContext.Provider>
    </div>
  );
}

import { BrowserRouter, Route, Routes } from "react-router-dom";
import LoginPage from "./components/UI/pages/LoginPage";
import MaintPage from "./components/UI/pages/MainPage";
import { AuthProvider, ProtectedRouter } from "./lib/auth";
import { MetaProvider } from "./lib/meta";


export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AuthProvider>
          <MetaProvider>
            <Routes>
              <Route path="/" element={
                <ProtectedRouter>
                  <MaintPage />
                </ProtectedRouter>
              } />
              <Route path="login" element={<LoginPage />} />
            </Routes>
          </MetaProvider>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

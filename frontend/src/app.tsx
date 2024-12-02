export function App() {
  return (
    <div className="px-12 h-screen flex flex-col">
      <header className="flex justify-between py-6">
        <div className="flex space-x-6">
          <div>Logo</div>
          <div>Restaurantes</div>
          <div>Seja Parceiro</div>
          <div>Fale conosco</div>
        </div>
        <div className="flex space-x-6">
          <div>Registre-se</div>
          <div>Login</div>
        </div>
      </header>
      <body className="flex flex-col space-x-6 space-y-6 py-6 flex-1 items-center justify-center">
        Página principal - Landing Page
        <img src="static/bg-logo.png" alt="LOGO" width={300} height={300} />
      </body>
      <footer className="flex py-6 justify-center">
        Footer
      </footer>
    </div>
  )
}

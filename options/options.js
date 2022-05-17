const styles = StyleSheet.create({
  hr: {
    marginTop: 20,
    marginBottom: 20,
    borderBottomColor: "black",
    borderBottomWidth: 1
  },
  container: { flex: 1, height: 100, padding: 13 },
  text: { color: "black", fontSize: 25 },
  buttonPressed: { backgroundColor: "#08090e" },
  buttonNotPressed: { backgroundColor: "#2fff00" },
  button: { borderRadius: 4, padding: 15, marginTop: 10 },
  buttonText: { color: "white", textAlign: "center", fontSize: 16 }
})

export const globalOptions = {
  name: "demo101_30437Identifier",
  url: "https://demo101_30437Identifier.botics.co",
  api: "https://demo101_30437Identifier.botics.co/api/v1"
}

export const modulesOptions = {
  "@modules/app-menu": {
    title: "Test Menu",
    copy: "Routes available",
    styles: styles
  }
}

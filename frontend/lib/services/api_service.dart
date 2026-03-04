import 'package:http/http.dart' as http;

Future<void> activateMode() async {
  await http.get(Uri.parse("http://IP_PC:5000/mode-on"));
}
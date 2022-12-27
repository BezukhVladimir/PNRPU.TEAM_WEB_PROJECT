<form action="#" method="post" target="_blank">
  <h2>Купить билет</h2>
  <fieldset>
    <legend>Персональные данные</legend>
    <ul>
      <li>
        <label for="name">Имя:*</label>
        <input type="text" name="name" placeholder="Иван Иванов" id="name" required>
      </li>
      <li>
        <label for="age">Возраст:</label>
        <input type="number" name="age" placeholder="27" id="age" min="0" max="125">
      </li>
    </ul>
  </fieldset>
  <p id="registration_button"></p>
  <button type="submit">Далее</button>
  <script src="query.js"></script>
  <p>* — Обязательные поля</p>
</form>
const tweetForm = document.querySelector("#tweet-form");
const tweetInput = document.querySelector("#tweet-input");
const tweetContainer = document.querySelector("#tweet-container");

tweetForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const tweet = document.createElement("div");
  tweet.classList.add("tweet");
  tweet.textContent = tweetInput.value;

  tweetContainer.prepend(tweet);

  tweetInput.value = "";
});
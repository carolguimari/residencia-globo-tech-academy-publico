package main

import (
	"math/rand"
	"net/http"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

var urlsBd map[string]string

type shortUrlInput struct {
	Url string `json:"url"`
}

const SHORT_URL_LENGHT = 6

func RandomString() string {
	charSet := "abcdedfghijklmnopqrst"
	var output strings.Builder
	length := SHORT_URL_LENGHT
	for i := 0; i < length; i++ {
		random := rand.Intn(len(charSet))
		randomChar := charSet[random]
		output.WriteString(string(randomChar))
	}
	return output.String()
}

func createShortUrl(c *gin.Context) {
	var newShortUrlInput shortUrlInput
	if err := c.ShouldBindJSON(&newShortUrlInput); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newShortUrlKey := RandomString()
	urlsBd[newShortUrlKey] = newShortUrlInput.Url

	c.JSON(http.StatusCreated, gin.H{
		"shortUrlKey": newShortUrlKey,
	})
}

func parseShortUrl(c *gin.Context) {

	shortUrlKey := c.Param("shortUrlKey")

	if originalUrl, exists := urlsBd[shortUrlKey]; exists {
		c.Header("Location", originalUrl)
		c.Status(http.StatusMovedPermanently)
		return
	}

	c.Status(http.StatusNotFound)
}

func main() {

	urlsBd = make(map[string]string)
	rand.Seed(time.Now().Unix())

	router := gin.Default()

	shortUrlRouter := router.Group("/surl")
	{
		shortUrlRouter.POST("/", createShortUrl)
		shortUrlRouter.GET("/:shortUrlKey", parseShortUrl)
	}

	router.Run()
}
